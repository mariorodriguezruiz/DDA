package a;
import java.util.ArrayList;
import java.lang.Math;

public class Main {	
	public static void main(String[] args) throws InterruptedException
    {
//		int tam = (int)Math.pow(10,9) ;
//		int tam = (int)Math.pow(10,8) ;
		int tam = (int)Math.pow(10,4) ;
		ArrayList<Integer> v1, v2, v3 ;
		int siz, rem_tam ;
		int NUM_TH = 8, pos_ini, pos_fin ;
		long start, end, time;
		ArrayL al = new ArrayL() ;
		
		v1 = al.RandArray(tam);
		Thread.sleep(1000);
		v2 = al.RandArray(tam);		
		v3 = al.InitializeArray(tam);
		
		System.out.print("\nSizeVector\tNumThreads\tTime(ms)\n");		
		
		for (int nt = 1; nt <= NUM_TH; nt++)
        {
			siz = v1.size()/nt ;      // work size for each thread
	        rem_tam = v1.size()%nt ;   // remainder of division
	        pos_ini = 0 ;
	        pos_fin = 0 ;
	        ArrayL resA = new ArrayL(v1.size()) ;
			
	        start = System.currentTimeMillis() ;   
	        for (int i = 0; i < nt; i++)
	        {
				pos_fin = pos_ini+siz ;  // final position is the sum of initial position and work size 
				AddTwoVectors ch = new AddTwoVectors(v1, v2, pos_ini, pos_fin);				
				ch.start() ;
				ch.join();
				resA.AddValorsInArray(ch.getResult(), pos_ini, pos_fin) ;
				pos_ini = pos_fin ;// update initial position for next thread
	        }
				//  When remainder is distint of zero
			if (rem_tam > 0){
				for (int j = 0; j < rem_tam; j++){
					pos_fin = pos_ini+1 ;
					AddTwoVectors ch1 = new AddTwoVectors(v1, v2, pos_ini, pos_fin);
					
					ch1.start() ;
					ch1.join();	
					resA.AddValorsInArray(ch1.getResult(), pos_ini, pos_fin) ;
					pos_ini = pos_fin ;
				}
			} 
			
			end = System.currentTimeMillis() ;
			time = (end-start);			
			v3 = resA.getResult() ;
			System.out.print(tam + "\t" + nt + "\t" + time + "\n");
        }
	     
		if(v1.size()<=10){
			al.PrintArray(v1) ;
			al.PrintArray(v2) ;
			al.PrintArray(v3) ;
		}
		
    }
}
