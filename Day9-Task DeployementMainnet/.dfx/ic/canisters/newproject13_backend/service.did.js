export const idlFactory = ({ IDL }) => {
  const MemberReward = IDL.Record({
    'memberId' : IDL.Principal,
    'points' : IDL.Nat,
  });
  const RewardProposal = IDL.Record({
    'id' : IDL.Nat,
    'votes' : IDL.Nat,
    'description' : IDL.Text,
    'retailer' : IDL.Principal,
    'approved' : IDL.Bool,
  });
  return IDL.Service({
    'addRewardPoints' : IDL.Func([IDL.Principal, IDL.Nat], [IDL.Bool], []),
    'approveProposal' : IDL.Func([IDL.Nat, IDL.Nat], [IDL.Bool], []),
    'getAllMemberRewards' : IDL.Func([], [IDL.Vec(MemberReward)], ['query']),
    'getAllProposals' : IDL.Func([], [IDL.Vec(RewardProposal)], ['query']),
    'getMemberRewards' : IDL.Func(
        [IDL.Principal],
        [IDL.Opt(MemberReward)],
        ['query'],
      ),
    'getProposal' : IDL.Func([IDL.Nat], [IDL.Opt(RewardProposal)], ['query']),
    'proposeReward' : IDL.Func([IDL.Principal, IDL.Text], [IDL.Nat], []),
    'redeemPoints' : IDL.Func([IDL.Principal, IDL.Nat], [IDL.Bool], []),
    'voteForProposal' : IDL.Func([IDL.Nat], [IDL.Bool], []),
  });
};
export const init = ({ IDL }) => { return []; };
