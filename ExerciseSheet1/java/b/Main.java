package b;
import java.util.ArrayList;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.lang.Math;
import java.util.Random;

public class Main {
	public static void PrintArray(ArrayList<Integer> vloc){
    	System.out.print("[");
    	for(int i = 0; i < vloc.size(); i++) {   
    	    System.out.print(vloc.get(i) + ", ");
    	}
    	System.out.print("]\n");
    }
	
	public static void main(String[] args) throws InterruptedException
    {
//		int tam = (int)Math.pow(10,9) ;
//		int tam = (int)Math.pow(10,8) ;
		int tam = (int)Math.pow(10,8) ;
		ArrayList<Integer> v1 = new ArrayList<Integer>(tam);
		int min_res = 0, siz, rem_tam ;
		int NUM_TH = 8, pos_ini, pos_fin ;
		long start, end, time;

		Lock lock = new ReentrantLock();

		Random rand = new Random();
		rand.setSeed(System.currentTimeMillis());
		for (int i=0; i<tam; i++)
		{	
			int r = rand.nextInt() %1000;
		    v1.add(r);
		}
		
		System.out.print("\nSizeVector\tMiniumNumber\tNumThreads\tTime(ms)\n");
		for (int nt = 1; nt <= NUM_TH; nt++)
        {
			siz = v1.size()/nt ;      // work size for each thread
	        rem_tam = v1.size()%nt ;   // remainder of division
    		min_res = v1.get(0) ;        // initialize minium result
	        pos_ini = 0 ;
	        pos_fin = 0 ;
			
	        start = System.currentTimeMillis() ;   
	        for (int i = 0; i < nt; i++)
	        {
				pos_fin = pos_ini+siz ;  // final position is the sum of initial position and work size 
				MiniumNumber ch = new MiniumNumber(v1, pos_ini, pos_fin, min_res);
				pos_ini = pos_fin ;// update initial position for next thread
				ch.start() ;
				ch.join();

    			// Critical section
    			lock.lock();
    			min_res = ch.getResult() ;
                lock.unlock();
                
				
	        }
				//  When remainder is distint of zero
			if (rem_tam > 0){
				for (int j = 0; j < rem_tam; j++){
					pos_fin = pos_ini+1 ;
					MiniumNumber ch1 = new MiniumNumber(v1, pos_ini, pos_fin, min_res);
					pos_ini = pos_fin ;
					ch1.start() ;
					ch1.join();	

	    			// Critical section
	    			lock.lock();
	    			min_res = ch1.getResult() ;
	                lock.unlock();
					
				}
				
			} 
			end = System.currentTimeMillis() ;
			time = (end-start);
			
			
			System.out.print(tam + "\t" + min_res + "\t" + nt + "\t" + time + "\n");
        }
		if(v1.size()<=10)
			PrintArray(v1) ;
		
    }
}
