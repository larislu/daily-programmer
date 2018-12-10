import java.util.Scanner;
import java.util.Random;
import java.util.List;
import java.util.Vector;
import java.io.File;
import java.io.FileNotFoundException;

class FalloutGame
{
    public static void main(String[] args)
    {
        Scanner s = new Scanner(System.in);
        System.out.println("Difficulty (1-5)?");
        int difficulty = s.nextInt();
        s.nextLine();

        int length = 0;
        Random rand = new Random(System.currentTimeMillis());

        switch(difficulty)
        {
            case 1:
                System.out.println("[Locked - Very Easy]");
                length = rand.nextInt(2) + 4;
                break;
            case 2:
                System.out.println("[Locked - Easy]");
                length = rand.nextInt(3) + 6;
                break;
            case 3:
                System.out.println("[Locked - Average]");
                length = rand.nextInt(2) + 9;
                break;
            case 4:
                System.out.println("[Locked - Hard]");
                length = rand.nextInt(2) + 11;
                break;
            case 5:
                System.out.println("Locked - Very Hard");
                length = rand.nextInt(3) + 13;
                break;
            
        }
        
        List<String> dictionary = new Vector();

        try
        {
            File f = new File("enable1.txt");
            Scanner reader = new Scanner(f);

            while (reader.hasNextLine())
            {
                String word = reader.nextLine();
                if (word.length() == length)
                {
                    dictionary.add(word);
                }
            }
        }
        catch(FileNotFoundException e)
        {
            System.out.println("An error occured.");
            e.printStackTrace();
        }

        System.out.println("ROBCO INDUSTRIES (TM) TERMLINK PROTOCOL");
        System.out.println("!!! WARNING: LOCKOUT IMMINENT !!!");

        List<String> wordsInGame = new Vector();

        for (int i = 0; i < 10; ++i)
        {
            int wordIndex = rand.nextInt(dictionary.size());
            wordsInGame.add(dictionary.get(wordIndex));
            System.out.println(dictionary.get(wordIndex).toUpperCase());

            dictionary.remove(wordIndex);
        }

        int randWord = rand.nextInt(wordsInGame.size());
        String trueWord = wordsInGame.get(randWord);
        boolean victory = false;
        System.out.println("ENTER PASSWORD NOW");

        for (int guesses = 1; guesses < 5; ++guesses)
        {
            String boxes = new String(new char[(5 - guesses)]).replace("\0", "[]");
            System.out.println((5 - guesses) + " ATTEMPT(S) LEFT: " + boxes);
            String input = s.nextLine();
            String playerGuess = input.toLowerCase();

            if (playerGuess.equals(trueWord))
            {
                System.out.println("Exact match!");
                System.out.println("Please wait while system is accessed.");
                victory = true;
                break;
            }

            int numCorrect = 0;
            for (int letter = 0; letter < trueWord.length() && letter < playerGuess.length(); ++letter)
            {
                if (playerGuess.charAt(letter) == trueWord.charAt(letter))
                {
                    ++numCorrect;
                }
            }
            System.out.println("Entry denied");
            System.out.println(numCorrect + "/" + trueWord.length() + " correct");
        }

        if (!victory)
        {
            System.out.println("Correct word was: " + trueWord.toUpperCase());
        }
    }
}



