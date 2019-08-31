//CETYS UNIVERSIDAD CAMPUS ENSENADA, INGENIERÍA EN SOFTWARE, PFR. CALEMAN
//package paqueteDondeMetisteEsto;

import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author Pablo A. Domínguez Medina
 */
public class cool_calculator {
    
    public static String zar;
    public static String sign;
    
    public static void main(String[] args) {
        Start();
    }
    
    public static void Start() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Binario o Decimal? Escriba B o D");
        String d = sc.nextLine();
        EspEntrada();
        String a, b, c, x;
        
        do {
            
            System.out.println("");
            a = sc.nextLine();
            System.out.println("");
            b = sc.nextLine();
            System.out.println("");
            c = sc.nextLine();
            System.out.println("");
            
            zar = (Integer.parseInt(a) - Integer.parseInt(c)) + "";
            sign = b;
            
            if (d.equalsIgnoreCase("d")) {
                DecimalStart(a, b, c);
            } else if (d.equalsIgnoreCase("b")) {
                BinaryStart(a, b, c);
            }
            
            System.out.println("Teclee C para continuar, cualquier otra para salir");
            x = sc.nextLine();
            
            cls();
            EspEntrada();
        } while (x.equalsIgnoreCase("c"));
        
        System.out.println("Fin del programa, recuerde ponerle un 10 a Pablo A. Domínguez Medina #9864");
        
    }
    
    public static void DecimalStart(String a, String b, String c) {
        String VA = Integer.toBinaryString(Integer.parseInt(a));
        String VC = Integer.toBinaryString(Integer.parseInt(c));
        BinaryStart(VA, b, VC);
    }
    
    public static void BinaryStart(String ValA, String Signo, String ValB) {
        String ValorA = Ajustar(Comparador(ValA, Signo, ValB), ValA);
        String ValorB = Ajustar(Comparador(ValA, Signo, ValB), ValB);
        if (Signo.equalsIgnoreCase("-")) {
            Resta(ValorA, ValorB);
        } else {
            Suma(ValorA, ValorB);
        }
    }
    
    public static char[] TC(String Ali) {
        char art[] = new char[Ali.length()];
        for (int i = 0; i < Ali.length(); i++) {
            art[i] = Ali.charAt(i);
        }
        
        return art;
    }
    
    public static void Resta(String A, String B) {
        char alpha[] = TC(A);
        char beta[] = TC(B);
        int dealer;
        String ard, arc;
        int comp = 0;
        char res[] = new char[A.length()];
        
        for (int i = A.length() - 1; i >= 0; i--) {
            ard = "" + alpha[i];
            arc = "" + beta[i];
            dealer = (Integer.parseInt(ard) - comp) - Integer.parseInt(arc);
            
            switch (dealer) {
                case 0:
                    res[i] = '0';
                    comp = 0;
                    break;
                case 1:
                    res[i] = '1';
                    comp = 0;
                    break;
                case -1:
                    res[i] = '1';
                    comp = 1;
                    break;
                case -2:
                    res[i] = '0';
                    comp = 1;
                default:
                    break;
            }
            Show(alpha, beta, res, comp, i);
        }
        
        SimpleShow(alpha, beta, res);
    }
    
    public static void Suma(String A, String B) {
        char alpha[] = TC(A);
        char beta[] = TC(B);
        int dealer;
        String ard, arc;
        int comp = 0;
        char res[] = new char[A.length()];
        
        for (int i = A.length() - 1; i >= 0; i--) {
            ard = "" + alpha[i];
            arc = "" + beta[i];
            dealer = Integer.parseInt(ard) + Integer.parseInt(arc) + comp;
            
            switch (dealer) {
                case 0:
                    res[i] = '0';
                    comp = 0;
                    break;
                case 1:
                    res[i] = '1';
                    comp = 0;
                    break;
                case 2:
                    res[i] = '0';
                    comp = 1;
                    break;
                case 3:
                    res[i] = '1';
                    comp = 1;
                    break;
                default:
                    break;
            }
            Show(alpha, beta, res, comp, i);
        }
        
        SimpleShow(alpha, beta, res);
    }
    
    public static char[] SimpleSuma(String A, String Bt) {
        String B = Ajustar(Comparador(A, "+", Bt), Bt);
        char alpha[] = TC(A);
        char beta[] = TC(B);
        int dealer;
        String ard, arc;
        int comp = 0;
        char res[] = new char[A.length()];
        
        for (int i = A.length() - 1; i >= 0; i--) {
            ard = "" + alpha[i];
            arc = "" + beta[i];
            dealer = Integer.parseInt(ard) + Integer.parseInt(arc) + comp;
            
            switch (dealer) {
                case 0:
                    res[i] = '0';
                    comp = 0;
                    break;
                case 1:
                    res[i] = '1';
                    comp = 0;
                    break;
                case 2:
                    res[i] = '0';
                    comp = 1;
                    break;
                case 3:
                    res[i] = '1';
                    comp = 1;
                    break;
                default:
                    break;
            }
        }
        
        return res;
    }
    
    public static void SimpleShow(char[] al, char[] be, char[] re) {
        System.out.println("  - R E S U L T A D O S - \n\n");
        System.out.print("\033[38m");
        for (int a = 0; a < al.length; a++) {
            System.out.print(al[a]);
        }
        
        System.out.println("");
        
        for (int a = 0; a < be.length; a++) {
            System.out.print(be[a]);
        }
        System.out.print("\033[33m");
        System.out.println("");
        
        for (int a = 0; a < be.length; a++) {
            System.out.print("-");
        }
        System.out.println("\033[32m");
        for (int a = 0; a < re.length; a++) {
            System.out.print(re[a]);
        }
        System.out.println("\033[33m\n\n");
        ShowData(re);
        System.out.print(Integer.parseInt(Chains(al), 2) + " " + sign + " " + Integer.parseInt(Chains(be), 2) + " = ");
        if (isWeak(Chains(al), Chains(be))) {
            System.out.println(zar);
        } else {
            System.out.println(Integer.parseInt(Chains(re), 2));
        }
        
        System.out.println("");
        
        for (int a = 0; a < be.length * 4; a++) {
            System.out.print("-");
        }
        System.out.println("");
        System.out.println("\033[37m" + ShowData(re) + "\n\n");
        
    }
    
    public static void Show(char[] al, char[] be, char[] re, int comp, int i) {
        
        System.out.println("  - R E S U L T A D O S - \n\n");
        
        for (int a = 0; a < al.length; a++) {
            if (a == i) {
                System.out.print("\033[32m" + comp + "\033[33m");
            } else {
                System.out.print(" ");
            }
        }
        
        System.out.println("");
        
        for (int a = 0; a < al.length; a++) {
            if (a == i) {
                System.out.print("\033[32m");
            }
            System.out.print(al[a]);
            System.out.print("\033[33m");
        }
        
        System.out.println("");
        
        for (int a = 0; a < be.length; a++) {
            if (a == i) {
                System.out.print("\033[32m");
            }
            System.out.print(be[a]);
            System.out.print("\033[33m");
        }
        
        System.out.println("");
        
        for (int a = 0; a < be.length; a++) {
            System.out.print("-");
        }
        
        System.out.println("");
        
        for (int a = 0; a < re.length; a++) {
            if (a == i) {
                System.out.print("\033[32m");
            }
            System.out.print(re[a]);
            System.out.print("\033[33m");
        }
        System.out.println("\n\n\n\n\n\n");
        System.out.println("\n\n");
        cls();
    }
    
    public static void cls() {
        try {
            Thread.sleep(250);
        } catch (InterruptedException ex) {
            Logger.getLogger(cool_calculator.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        System.out.println("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
    }
    
    public static int Comparador(String ValA, String Signo, String ValB) {
        int al = 1;
        if (Signo.equalsIgnoreCase("-")) {
            al++;
        }
        if (ValA.length() > ValB.length()) {
            al += ValA.length();
        } else {
            al += ValB.length();
        }
        return al;
    }
    
    public static String Ajustar(int length, String caso) {
        char ch[] = new char[length];
        int c = 0;
        while (c < length) {
            if (c < (length - caso.length())) {
                ch[c] = '0';
            } else {
                ch[c] = caso.charAt(c - (length - caso.length()));
            }
            c++;
        }
        return Chains(ch);
    }
    
    public static String Chains(char[] ch) {
        String gotcha = "";
        for (int i = 0; i < ch.length; i++) {
            gotcha = gotcha + "" + ch[i];
        }
        return gotcha;
    }
    
    public static Boolean isWeak(String A, String B) {
        int na = Integer.parseInt(A, 2);
        int nb = Integer.parseInt(B, 2);
        
        if (na - nb < 0) {
            return true;
        } else {
            return false;
        }
    }

    /*public static String ItalianAppetizer(char[] rek) {
        char[] re = rek;
        int c = 0;
        for (int i = 0; i < re.length; i++) {
            if (re[i] == 0) {
                re[i] = 1;
            } else {
                re[i] = 0;
            }
        }
        System.out.println("Error final");
        re = SimpleSuma(Chains(re), "1");

        return Chains(re);
    }*/
    public static String ShowData(char[] ch) {
        String value = "";
        int c = 0;
        int d = 0;
        int aux = 0;
        for (int i = ch.length - 1; i >= 0; i--) {
            aux = (int) (Integer.parseInt(ch[i] + "") * Math.pow(2, c));
            if (i == 0) {
                if (sign.equalsIgnoreCase("-")) {
                    value += "(-" + aux + ")";
                    d += -aux;
                } else {
                    value += aux;
                    d += aux;
                }
            } else {
                value += aux + " + ";
                d += aux;
            }
            c++;
        }
        value = value + " = " + d;
        
        zar = d + "";
        
        return value;
    }
    
    public static void EspEntrada() {
        System.out.println("Escribe valores de la siguiente forma:");
        System.out.println("XXXXXX");
        System.out.println("+/-");
        System.out.println("XXXXXX");
        System.out.println("------");
        System.out.println("");
    }
}
