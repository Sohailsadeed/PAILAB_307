package com.email.writer.dtos;

import java.time.LocalDateTime;


import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Lob;
import jakarta.persistence.Table;

@Entity
@Table(name="email_logs")
public class EmailEntity {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private int id;
	@Lob
	@Column(name = "request", columnDefinition = "LONGTEXT")
	private String emailRequest;
	@Lob
	@Column(name = "response",columnDefinition = "LONGTEXT")
	private String emailResponse;
	@Column(name = "Date")
	private LocalDateTime date;
	
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getEmailRequest() {
		return emailRequest;
	}
	public void setEmailRequest(String emailRequest) {
		this.emailRequest = emailRequest;
	}
	public String getEmailResponse() {
		return emailResponse;
	}
	public void setEmailResponse(String emailResponse) {
		this.emailResponse = emailResponse;
	}
	public LocalDateTime getDate() {
		return date;
	}
	public void setDate(LocalDateTime date) {
		this.date = date;
	}
	
}
