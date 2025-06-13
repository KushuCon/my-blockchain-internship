import type { Principal } from '@dfinity/principal';
import type { ActorMethod } from '@dfinity/agent';
import type { IDL } from '@dfinity/candid';

export interface MemberReward { 'memberId' : Principal, 'points' : bigint }
export interface RewardProposal {
  'id' : bigint,
  'votes' : bigint,
  'description' : string,
  'retailer' : Principal,
  'approved' : boolean,
}
export interface _SERVICE {
  'addRewardPoints' : ActorMethod<[Principal, bigint], boolean>,
  'approveProposal' : ActorMethod<[bigint, bigint], boolean>,
  'getAllMemberRewards' : ActorMethod<[], Array<MemberReward>>,
  'getAllProposals' : ActorMethod<[], Array<RewardProposal>>,
  'getMemberRewards' : ActorMethod<[Principal], [] | [MemberReward]>,
  'getProposal' : ActorMethod<[bigint], [] | [RewardProposal]>,
  'proposeReward' : ActorMethod<[Principal, string], bigint>,
  'redeemPoints' : ActorMethod<[Principal, bigint], boolean>,
  'voteForProposal' : ActorMethod<[bigint], boolean>,
}
export declare const idlFactory: IDL.InterfaceFactory;
export declare const init: (args: { IDL: typeof IDL }) => IDL.Type[];
