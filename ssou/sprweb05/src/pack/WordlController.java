package pack;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.mvc.Controller;

public class WordlController implements Controller{
	@Override
	public ModelAndView handleRequest(HttpServletRequest arg0, HttpServletResponse arg1) throws Exception {
		System.out.println("WorldController ó��");
		
		ModelAndView view = new ModelAndView();
		view.setViewName("list2");
		view.addObject("msg", "����");
		
		return view;
	}
}
