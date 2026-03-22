#pragma once

#include <Nerve/alActorStateBase.h>
#include <math/seadVector.h>

class EnemyStateHipDropDownParam;

class EnemyStateHipDropDown : public al::ActorStateBase
{
private:
        EnemyStateHipDropDownParam* mParam;
        sead::Vector3f              _14;
        const char*                 mAnimName;
        void*                       _24;
        void*                       _28;

public:
        EnemyStateHipDropDown( al::LiveActor* host, EnemyStateHipDropDownParam* blowDownParam, const char*, int );
};
