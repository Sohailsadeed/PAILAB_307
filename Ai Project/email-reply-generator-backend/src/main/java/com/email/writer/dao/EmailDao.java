package com.email.writer.dao;

import org.springframework.data.jpa.repository.JpaRepository;

import com.email.writer.dtos.EmailEntity;

public interface EmailDao extends JpaRepository<EmailEntity,Integer>{
	
}
