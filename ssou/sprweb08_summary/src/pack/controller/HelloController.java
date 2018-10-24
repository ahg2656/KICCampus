package pack.controller;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.mvc.Controller;

import pack.model.HelloModel;

public class HelloController implements Controller{
	private HelloModel helloModel;
	
	public void setHelloModel(HelloModel helloModel) {
		this.helloModel = helloModel;
	}
	
	@Override
	public ModelAndView handleRequest(HttpServletRequest arg0, HttpServletResponse arg1) throws Exception {
		//ModelAndView view = new ModelAndView();
		
		//�� ����
		String ss = helloModel.process();
		
		ModelAndView view = new ModelAndView();
		view.addObject("result", ss);
		
		view.setViewName("hello");	//���� ���� (forward ���)
		//view.setViewName("redirect:/views/hello.jsp");	//ViewReslover �� ��ġ�� �ʱ� ������ ��Ȯ�� ��� �ʿ�(redirect ���)
		
		
		return view;
	}
}
