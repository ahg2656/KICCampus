package pack.aspect;

import org.springframework.stereotype.Component;

@Component
public class SecurityClass {
	public void mySecurity() {
		System.out.println("핵심 메소드 수행 전에 보안 설정");
	}
}
