	package com.email.writer.aop;
	
	import org.aspectj.lang.ProceedingJoinPoint;
	import org.aspectj.lang.annotation.Around;
	import org.aspectj.lang.annotation.Aspect;
	import org.slf4j.Logger;
	import org.slf4j.LoggerFactory;
	import org.springframework.stereotype.Component;
	
	import jakarta.annotation.PostConstruct;
	
	
	@Aspect
	@Component
	public class LoggingAspects {
		@PostConstruct
		public void init() {
		    System.out.println("LoggingAspect Loaded");
		}
		private static final Logger logger = LoggerFactory.getLogger(LoggingAspects.class);
		
		@Around("execution(* com.email.writer.services.*.*(..))")
		public Object logEmail(ProceedingJoinPoint joinPoint) throws Throwable{
			logger.info("Method called: {}",joinPoint.getSignature());
			long start = System.currentTimeMillis();
			Object result = joinPoint.proceed();
			long executionTime =  System.currentTimeMillis() - start;
			logger.info("executed in "+executionTime+" ms");
			return result;
		}
	}
		