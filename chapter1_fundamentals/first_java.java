import java.util.Arrays;

public class BinarySearch 
{
    public static int rank(int key, int [] a)
    {
        int lo =0;
        int hi = a.length -1;
        while (lo <= hi)
        {
            int mid = lo +(hi - lo) /2;
            if (key < a[mid]) hi = mide -1;
            else if (key > a[mid]) lo = mid + 1;
            else        return mid;
        }
        return -1
    }
}


public staticvoid main(string[] args)
{
    int[] whiltelist = In.readIns(args[0]);
    Arrays.sort(whiltelist);

    while (!StdIn.isEmpty())
    {
        int key = StdIn.readInt();
        if (rank(key,whiltelist) == -1)
            StdOut.print(key)
    }
}