package a;

import java.util.ArrayList;
import java.util.Random;

public class ArrayL {
	private ArrayList<Integer> res ;
	
	public ArrayL(){
	}
	
	public ArrayL(int tam){
		res = new ArrayList<Integer>(tam);
		this.Initialize(tam);
	}
	
	public void Initialize(int tam){
    	for(int i=0; i<tam;i++)
    		res.add(0);
    }
	
	public ArrayList<Integer> InitializeArray(int tam){
    	ArrayList<Integer> vloc = new ArrayList<Integer>(tam);
    	for(int i=0; i<vloc.size();i++)
    		vloc.add(0);
    	return vloc ;
    }
	
	public void AddValorsInArray(ArrayList<Integer> vloc, int pos_ini, int pos_fin){
		for(int i=pos_ini; i<pos_fin;i++){
    		res.set(i, vloc.get(i));
		}
    }
    
    public ArrayList<Integer> getResult(){
    	return res ;
    }
    
    public void PrintArray(ArrayList<Integer> vloc){
    	System.out.print("[");
    	for(int i = 0; i < vloc.size(); i++) {   
    	    System.out.print(vloc.get(i) + ", ");
    	}
    	System.out.print("]\n");
    }
	
	public ArrayList<Integer> RandArray(int tam){
		Random rand = new Random();
		ArrayList<Integer> v1 = new ArrayList<Integer>(tam);
		rand.setSeed(System.currentTimeMillis());
		for (int i=0; i<tam; i++)
		{	
			int r;
			do{
				r = rand.nextInt() % 10;
			}while(r<=0);
		    v1.add(r);
		}
		return v1; 
	}
}
