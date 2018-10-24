package pack.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import pack.model.HelloModel;

@Controller
//@RequestMapping("hello.do")
@RequestMapping({"world.do","h*,kbs/abc","mbc","sbs"})
public class HelloController{
	@Autowired
	private HelloModel helloModel;
	
	
	/*@RequestMapping(method=RequestMethod.GET)
	public ModelAndView abc() {
		//ModelAndView view = new ModelAndView();
		
		//�� ����
		String ss = helloModel.process();
		
		ModelAndView view = new ModelAndView();
		view.addObject("result", ss);
		
		view.setViewName("hello");	//���� ���� (forward ���)
		//view.setViewName("redirect:/views/hello.jsp");	//ViewReslover �� ��ġ�� �ʱ� ������ ��Ȯ�� ��� �ʿ�(redirect ���)
		
		
		return view;
	}*/
	
	/*@RequestMapping(method=RequestMethod.GET)
	public Map<String, Object> abc() {
		String ss = helloModel.process();
		
		HashMap<String, Object> map = new HashMap<>();
		map.put("result", ss);
		//��û���� �����ϸ����� ����
		
		return map;
	}*/
	
	@RequestMapping(method=RequestMethod.GET)
	public Model abc(Model model) {
		String ss = helloModel.process();
		model.addAttribute("result", ss);
		//��û���� �����ϸ����� ����
	
		return model;
	}
}
