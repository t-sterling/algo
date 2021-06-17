package program;

import java.util.Stack;

public class TheTowerOfHanoi {

	private static final String LINE = "------------------------";

	private Stack<Integer> src;
	private Stack<Integer> aux;
	private Stack<Integer> des;
	private int n;

	public static void main(String [] args){
		TheTowerOfHanoi tower = new TheTowerOfHanoi(5);
		tower.solve();
	}

	TheTowerOfHanoi(int n){

		this.n = n;
		src = new Stack<>();
		aux = new Stack<>();
		des = new Stack<>();

		for(int i=n;i>0;i--){

			src.add(i);

		}

	}


	void solve(){
		solve(n, src,aux,des);
	}

	void solve(int i,
	           Stack<Integer> src,
	           Stack<Integer> aux,
	           Stack<Integer> des){

		if (i > 0){

			solve(i-1, src, des, aux);

			des.push(src.pop());

			System.out.println(LINE);
			System.out.println(src);
			System.out.println(aux);
			System.out.println(des);
			System.out.println(LINE);

			solve(i-1, aux, src, des);

		}

	}

}