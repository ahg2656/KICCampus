package pack;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class TestController{
	@RequestMapping("index.do")
	public ModelAndView abc() {
		System.out.println("TestController ����");
		//return new ModelAndView("list");
		
		ModelAndView view = new ModelAndView();
		view.setViewName("list");
		view.addObject("say", "������ �� ������̼�");	//request.getAttribute("say") �� ��û
		return view;
	}
}
