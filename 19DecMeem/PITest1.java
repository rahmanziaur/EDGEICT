import java.io.PrintStream;

public class PITest1 {
    // Create a custom wrapper class for PrintStream
    public static class PrintWrapper {
        private final PrintStream out;

        public PrintWrapper(PrintStream out) {
            this.out = out;
        }

        // Shorthand for println()
        public void p(Object obj) {
            out.println(obj);
        }

        // Shorthand for print() (if needed)
        public void pNoLn(Object obj) {
            out.print(obj);
        }
    }

    // Use the custom wrapper
    public final static PrintWrapper o = new PrintWrapper(System.out);

    public static void main(String[] args) {
        o.p(Math.PI); // Calls println()
        o.pNoLn("This is "); // Calls print()
        o.p("a test."); // Calls println()
    }
}
