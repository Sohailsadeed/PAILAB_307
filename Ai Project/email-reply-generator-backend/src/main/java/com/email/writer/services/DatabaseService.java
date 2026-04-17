package com.email.writer.services;

import org.springframework.stereotype.Service;

import com.email.writer.dao.EmailDao;
import com.email.writer.dtos.EmailEntity;

@Service
public class DatabaseService {
	
	 private final EmailDao emailDao;
	 public DatabaseService(EmailDao emailDao) {
			this.emailDao = emailDao;
	    }
	public void saveData(EmailEntity emailObject) {
		try {
		emailDao.save(emailObject);
		}
		catch(Exception e) {
			e.printStackTrace();
		}
	}
}
