package com.email.writer.services;

import java.time.LocalDateTime;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpStatusCode;
import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.client.WebClient;

import com.email.writer.dtos.Content;
import com.email.writer.dtos.EmailEntity;
import com.email.writer.dtos.GeminiRequest;
import com.email.writer.dtos.GeminiResponse;
import com.email.writer.dtos.Part;

@Service
public class EmailService {

	 private final WebClient webClient;
	 @Autowired
	 private DatabaseService DbService;
	    @Value("${gemini.api.key}")
	    private String apiKey;

	    public EmailService(WebClient webClient) {
	        this.webClient = webClient;
	    }
	    
	    public String generateReply(String prompt) {
	    	String emailContent = buildPrompt(prompt);
	        Part part = new Part(emailContent);
	        Content content = new Content(List.of(part));
	        GeminiRequest request = new GeminiRequest(List.of(content));
	        GeminiResponse response = webClient.post()
	                .uri(uriBuilder -> uriBuilder
	                        .queryParam("key", apiKey)
	                        .build())
	                .bodyValue(request)
	                .retrieve()
	                .onStatus(HttpStatusCode::isError,
	                        clientResponse -> clientResponse.bodyToMono(String.class)
	                                .map(RuntimeException::new))
	                .bodyToMono(GeminiResponse.class)
	                .block();

	        String reply =  response.getCandidates()
	                .get(0)
	                .getContent()
	                .getParts()
	                .get(0)
	                .getText();
	        
	        EmailEntity emailObject = new EmailEntity();
	        emailObject.setEmailRequest(prompt);
	        emailObject.setEmailResponse(reply);
	        emailObject.setDate(LocalDateTime.now());
	        DbService.saveData(emailObject);
	        
	        return reply;
	    }

		private String buildPrompt(String prompt) {
			StringBuilder createdPrompt = new StringBuilder();
			createdPrompt.append("Generate one professional email reply with the relying format for the following email. Do not generate the subject line");
			createdPrompt.append("/nThe email is:\n");
			createdPrompt.append(prompt);
			
			return createdPrompt.toString();
		}
	}
