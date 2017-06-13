package a;

import java.util.ArrayList;

public class AddTwoVectors extends Thread{
	private ArrayList<Integer> v1, v2 ;
	private int pos_ini, pos_fin ;
	private ArrayList<Integer> res ;
    
    public AddTwoVectors(ArrayList<Integer> vloc, ArrayList<Integer> vloc2, int pos_ini, int pos_fin)
    {
        this.v1 = vloc ;
        this.v2 = vloc2 ;
        this.pos_ini = pos_ini ;
        this.pos_fin = pos_fin ;
        this.res = new ArrayList<Integer>(vloc.size());
        this.InitializeArray();
    }
    
    public void InitializeArray(){
    	for(int i=0; i<v1.size();i++)
    		res.add(0);
    }
    
    public ArrayList<Integer> getResult(){
    	return res ;
    } 
    
    public void run()
    {   
    	for(int i=pos_ini; i < pos_fin ; i++){
    		res.set(i, v1.get(i)+v2.get(i)) ;
    	}
    }
}
