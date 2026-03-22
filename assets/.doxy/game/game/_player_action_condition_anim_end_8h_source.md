

# File PlayerActionConditionAnimEnd.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Player**](dir_c3d399ad73eabae4c9209488b7fe7035.md) **>** [**PlayerActionConditionAnimEnd.h**](_player_action_condition_anim_end_8h.md)

[Go to the documentation of this file](_player_action_condition_anim_end_8h.md)


```C++
#pragma once

#include "Player/PlayerActionMultiCondition.h"

class IUsePlayerAnimator;

class PlayerActionConditionAnimEnd : public PlayerActionCondition
{
private:
        const char*         mAnimName;
        IUsePlayerAnimator* mUsePlayerAnimator;
        int                 mAnimEndFrame;

public:
        virtual bool check();

public:
        PlayerActionConditionAnimEnd( IUsePlayerAnimator* animator, const char* animName, int animEndFrame );
};
```


