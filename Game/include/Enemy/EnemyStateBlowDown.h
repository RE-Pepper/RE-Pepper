#pragma once

#include <Nerve/alActorStateBase.h>
#include <math/seadVector.h>

class EnemyStateBlowDownParam;

class EnemyStateBlowDown : public al::ActorStateBase
{
private:
        EnemyStateBlowDownParam* mParam;
        sead::Vector3f           _14;
        const char*              mAnimName;
        void*                    _24;

public:
        EnemyStateBlowDown( al::LiveActor* host, EnemyStateBlowDownParam* blowDownParam, const char*, int );
};
