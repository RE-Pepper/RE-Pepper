#pragma once

#include <Nerve/alActorStateBase.h>

class WalkerStateParam;
class WalkerStateWanderParam;

class WalkerStateWander : public al::ActorStateBase
{
private:
        sead::Vector3f*               mFrontPtr;
        void*                         _14;
        const WalkerStateParam*       mWalkerParam;
        const WalkerStateWanderParam* mWanderParam;

public:
        WalkerStateWander( al::LiveActor* host, sead::Vector3f* frontPtr, const WalkerStateParam* walkerParam, const WalkerStateWanderParam* wanderParam );
};
