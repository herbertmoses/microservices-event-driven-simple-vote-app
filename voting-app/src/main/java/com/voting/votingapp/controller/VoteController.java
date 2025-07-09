package com.voting.votingapp.controller;

import com.voting.votingapp.model.Vote;
import com.voting.votingapp.service.VoteService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
import org.springframework.ui.Model;
import org.springframework.web.client.RestTemplate;

import java.util.Map;

@Controller
public class VoteController {

    private final VoteService voteService;
    private final RestTemplate restTemplate = new RestTemplate();

    @Autowired
    public VoteController(VoteService voteService) {
        this.voteService = voteService;
    }

    @GetMapping("/vote")
    public String showVoteForm(@RequestParam("username") String username, Model model) {
        // Fetch session data from Flask
        String flaskUrl = "http://localhost:5001/session/" + username;
        Map<String, Object> sessionData = null;

        try {
            sessionData = restTemplate.getForObject(flaskUrl, Map.class);
        } catch (Exception e) {
            System.out.println("Failed to retrieve session: " + e.getMessage());
        }

        model.addAttribute("username", username);
        model.addAttribute("session", sessionData);

        return "vote";
    }

    @PostMapping("/vote")
    public String submitVoteForm(@RequestParam("candidate") String candidate,
                                 @RequestParam("username") String username) {
        Vote vote = new Vote();
        vote.setCandidate(candidate);
        vote.setUserId(username); // now uses actual user
        vote.setTimestamp(System.currentTimeMillis());
        voteService.submitVote(vote);
        return "redirect:/vote?username=" + username;
    }

    // Optional REST API
    @ResponseBody
    @PostMapping("/api/vote")
    public Vote submitVoteApi(@RequestBody Vote vote) {
        vote.setTimestamp(System.currentTimeMillis());
        return voteService.submitVote(vote);
    }
}
