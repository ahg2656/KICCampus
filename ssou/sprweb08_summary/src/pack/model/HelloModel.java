package pack.model;

import java.util.Calendar;

public class HelloModel {
	public String process() {
		int hour = Calendar.getInstance().get(Calendar.HOUR_OF_DAY);
		
		if(hour >= 6 && hour <= 10) {
			return "���� ��ħ�Դϴ�."; 
		} else if(hour >= 12 && hour <= 15) {
			return "�����ϼ���.";
		} else {
			return "�ȳ��ϼ���.";
		}		
	}
}
