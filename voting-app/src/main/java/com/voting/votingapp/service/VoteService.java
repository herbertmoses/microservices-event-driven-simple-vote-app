package com.voting.votingapp.service;

import com.voting.votingapp.model.Vote;
import com.voting.votingapp.repository.VoteRepository;
import org.springframework.stereotype.Service;

@Service
public class VoteService {
    private final VoteRepository voteRepository;

    public VoteService(VoteRepository voteRepository) {
        this.voteRepository = voteRepository;
    }

    public Vote submitVote(Vote vote) {
        return voteRepository.save(vote);
    }
}
