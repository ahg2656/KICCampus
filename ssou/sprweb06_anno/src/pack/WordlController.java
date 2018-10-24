package pack;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

@Controller
@RequestMapping("world.do")
public class WordlController {
	@RequestMapping(method=RequestMethod.GET)	//get ���
	public ModelAndView sbs() {
		System.out.println("WorldController ó��");
		
		ModelAndView view = new ModelAndView();
		view.setViewName("list2");
		view.addObject("msg", "����:get");
		
		return view;
	}
	
	@RequestMapping(method=RequestMethod.POST)	//post ���
	public ModelAndView ytn() {
		System.out.println("WorldController ó��");
		
		ModelAndView view = new ModelAndView();
		view.setViewName("list2");
		view.addObject("msg", "����:post");
		
		return view;
	}
}
