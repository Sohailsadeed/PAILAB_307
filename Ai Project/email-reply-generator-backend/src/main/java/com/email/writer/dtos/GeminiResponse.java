package com.email.writer.dtos;

import java.util.List;

import lombok.Data;

@Data
public class GeminiResponse {
    private List<Candidate> candidates;
}


