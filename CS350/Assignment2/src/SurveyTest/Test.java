package SurveyTest;

import IO.*;
import Question.*;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.HashMap;

public class Test extends Survey implements Serializable {
    protected HashMap<Question, Response> questionCorrectResponses;
    protected ArrayList<Response> correctResponses;

    public Test(){
        this.questions = new ArrayList<Question>();
        this.responses = new ArrayList<Response>();
        this.questionCorrectResponses = new HashMap<Question, Response>();
        this.correctResponses = new ArrayList<Response>();
    }

    public Test(String name){
        this.name = name;
        this.questions = new ArrayList<Question>();
        this.responses = new ArrayList<Response>();
        this.questionCorrectResponses = new HashMap<Question, Response>();
        this.correctResponses = new ArrayList<Response>();
    }

    public static Test create(String name){
        return new Test(name);
    }

    public void displayTest(){
        Output.printString("Test: " + this.name);
        for (Question question : this.questions){
            question.displayQuestion();
//            if(question instanceof EssayQ || question instanceof ShortAnswerQ){
//                Output.printString("There's no correct ");
//            }
            Output.printStringNoLine("The correct answer is ");
            this.questionCorrectResponses.get(question).displayResponse();
        }
        Output.printString("");
    }

    public void addTFQ(){
        Output.printString("Enter the prompt for your True/False Question:");
        String qPrompt = Input.getInputString();
        TrueFalseQ trueFalseQ = new TrueFalseQ(qPrompt);
        Output.printString("Enter correct choice:");
        String qCorrectAnswerString = Input.getInputString();
        Response correctResponse = new Response(qCorrectAnswerString);
        this.questions.add(trueFalseQ);
        this.questionCorrectResponses.put(trueFalseQ,correctResponse);
        Output.printString("True/False Question Added.\n");
    }

    public void addMCQ(){
        Output.printString("Enter the prompt for your Multiple-Choice Question:");
        String qPrompt =  Input.getInputString();
        Output.printString("Enter the number of choices for your Multiple-Choice Question:");
        int qNumberOfChoices = Input.getInputInteger();
        ArrayList<String> choices = new ArrayList<String>();
        for(int i = 1; i <= qNumberOfChoices; i++){
            Output.printString("Enter choice #"+i);
            String choice = Input.getInputString();
            choices.add(choice);
        }
        MCQ mcq = new MCQ(qPrompt, choices);
        Output.printString("Enter correct choice:");
        String qCorrectAnswerString = Input.getInputString();
        Response correctResponse = new Response(qCorrectAnswerString);
        this.questions.add(mcq);
        this.questionCorrectResponses.put(mcq, correctResponse);
        Output.printString("Multiple-Choice Question Added.\n");
    }

    public void addShortAnswerQ(){
        Output.printString("Enter the prompt for your Short Answer Question:");
        String qPrompt = Input.getInputString();
        Output.printString("Enter the size for your Short Answer Question (not over than 150):");
        int qSize = Input.getInputInteger();
        Output.printString("Enter the number of responses for your Short Answer Question:");
        int qNumOfResp = Input.getInputInteger();
        ShortAnswerQ shortAnswerQ = new ShortAnswerQ(qPrompt, qSize,qNumOfResp);
        this.questions.add(shortAnswerQ);
        Response qCorrectAnswerString = new Response("Nothing. There is no correct answer.");
        this.questionCorrectResponses.put(shortAnswerQ, qCorrectAnswerString);
        Output.printString("Short-Answer Question Added.\n");
    }

    public void addEssayQ(){
        Output.printString("Enter the prompt for your Essay Question:");
        String qPrompt = Input.getInputString();
        Output.printString("Enter the size for your Essay Question:");
        int qSize = Input.getInputInteger();
        Output.printString("Enter the number of responses for your Essay Question:");
        int qNumOfResp = Input.getInputInteger();
        EssayQ essayQ = new EssayQ(qPrompt, qSize, qNumOfResp);
        this.questions.add(essayQ);
        Response qCorrectAnswerString = new Response("Nothing. There is no correct answer.");
        this.questionCorrectResponses.put(essayQ, qCorrectAnswerString);
        Output.printString("Essay Question Added.\n");
    }

    public void addRankingQ(){
        Output.printString("Enter the prompt for your Ranking Question:");
        String qPrompt = Input.getInputString();
        Output.printString("Enter the number of items for your Ranking Question:");
        int qNumberOfItems = Input.getInputInteger();
        ArrayList<String> items = new ArrayList<String>();
        for(int i = 1; i <= qNumberOfItems; i++){
            Output.printString("Enter item #"+i);
            String item = Input.getInputString();
            items.add(item);
        }
        RankingQ rankingQ = new RankingQ(qPrompt, items);
        Output.printString("Enter correct answer (line after line):");
        ArrayList<String> qCorrectAnswerArrayList = new ArrayList<String>();
        for(int i = 1; i <= qNumberOfItems; i++){
            String string = Input.getInputString();
            qCorrectAnswerArrayList.add(string);
        }
        Response correctResponse = new Response(qCorrectAnswerArrayList);
        this.questions.add(rankingQ);
        this.questionCorrectResponses.put(rankingQ,correctResponse);
        Output.printString("Ranking Question Added.\n");
    }

    public void addMatchingQ(){
        Output.printString("Enter the prompt for your Matching Question:");
        String qPrompt = Input.getInputString();
        Output.printString("Enter the number of items for your Matching Question");
        int qNumberOfItems = Input.getInputInteger();
        ArrayList<String> ll = new ArrayList<String>();
        Output.printString("Enter items for your left hand side list:");
        for(int i = 1; i <= qNumberOfItems; i++){
            Output.printString("Enter item #"+i);
            String item = Input.getInputString();
            ll.add(item);
        }
        ArrayList<String> rl = new ArrayList<String>();
        Output.printString("Enter items for your right hand side list:");
        for(int i = 1; i <= qNumberOfItems; i++){
            Output.printString("Enter item #"+i);
            String item = Input.getInputString();
            rl.add(item);
        }
        MatchingQ matchingQ = new MatchingQ(qPrompt, ll, rl);
        Output.printString("Enter correct answer (line after line):");
        ArrayList<String> qCorrectAnswerArrayList = new ArrayList<String>();
        for(int i = 1; i <= qNumberOfItems; i++){
            String string = Input.getInputString();
            qCorrectAnswerArrayList.add(string);
        }
        Response correctResponse = new Response(qCorrectAnswerArrayList);
        this.questions.add(matchingQ);
        this.questionCorrectResponses.put(matchingQ,correctResponse);
        Output.printString("Matching Question Added.\n");
    }
}
