package pack;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.mvc.Controller;

public class TestController implements Controller{
	@Override
	public ModelAndView handleRequest(HttpServletRequest arg0, HttpServletResponse arg1) throws Exception {
		System.out.println("TestController ����");
		//return new ModelAndView("list");
		
		ModelAndView view = new ModelAndView();
		view.setViewName("list");
		view.addObject("say", "������ ���̿� �����϶�!");
		return view;
	}
}
