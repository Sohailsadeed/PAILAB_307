package com.email.writer.dtos;

import lombok.Data;

@Data
public class EmailRequest {
	public String emailContent;
	public String tone;
}
