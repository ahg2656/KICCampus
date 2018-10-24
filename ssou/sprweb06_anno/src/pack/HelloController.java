package pack;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class HelloController {
	@RequestMapping("hello.do")	//get �� post �� �������� ����
	//@RequestMapping(value="hello.do", method=RequestMethod.GET)	//get ���
	public ModelAndView kbs() {
		System.out.println("HelloController ó��");
		
		ModelAndView view = new ModelAndView();
		view.setViewName("list1");
		view.addObject("msg", "��ο�");
		
		return view;
	}
}
