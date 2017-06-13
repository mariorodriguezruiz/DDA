package c;

import java.util.ArrayList;

public class Average extends Thread{
	private ArrayList<Integer> v ;
	private int pos_ini, pos_fin ;
	private double res ;
    
    public Average(ArrayList<Integer> vloc, int pos_ini, int pos_fin, double res)
    {
        v = vloc ;
        this.pos_ini = pos_ini ;
        this.pos_fin = pos_fin ;
        this.res = res ;
    }
    
    public double getResult(){
    	return res ;
    }    
    
    public void run()
    {   
    	int sum = 0 ;
    	for(int i=pos_ini; i < pos_fin ; i++){
    			sum += v.get(i) ;    		
    	}
		res = sum/(double)(v.size()) ;
    }
}
