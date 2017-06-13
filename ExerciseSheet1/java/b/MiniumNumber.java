package b;

import java.util.ArrayList;

public class MiniumNumber extends Thread{
	private ArrayList<Integer> v ;
	private int pos_ini, pos_fin ;
	private int res ;
    
    public MiniumNumber(ArrayList<Integer> vloc, int pos_ini, int pos_fin, int res)
    {
        v = vloc ;
        this.pos_ini = pos_ini ;
        this.pos_fin = pos_fin ;
        this.res = res ;
    }
    
    public int getResult(){
    	return res ;
    }    
    
    public void run()
    {   
    	for(int i=pos_ini; i < pos_fin ; i++){
    		if(v.get(i)<res){
    			res = v.get(i) ;
    		}
    	}
    }
}
