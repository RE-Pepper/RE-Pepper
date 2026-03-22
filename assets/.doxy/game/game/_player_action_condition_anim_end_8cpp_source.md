

# File PlayerActionConditionAnimEnd.cpp

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**src**](dir_47d28cd3eb946f860e1fe0f4e720b9c2.md) **>** [**Player**](dir_9f791c72b7e31512581b67600bde1506.md) **>** [**PlayerActionConditionAnimEnd.cpp**](_player_action_condition_anim_end_8cpp.md)

[Go to the documentation of this file](_player_action_condition_anim_end_8cpp.md)


```C++
#include "Player/PlayerActionConditionAnimEnd.h"

#include "Player/PlayerAnimator.h"

PlayerActionConditionAnimEnd::PlayerActionConditionAnimEnd( IUsePlayerAnimator* animator,
        const char*                                                             animName,
        int                                                                     animEndFrame )
    : mAnimName( animName ), mUsePlayerAnimator( animator ), mAnimEndFrame( animEndFrame )
{
}

bool PlayerActionConditionAnimEnd::check()
{
        if ( mAnimName )
        {
                if ( !( mUsePlayerAnimator->isAnim( mAnimName ) && !mUsePlayerAnimator->isAnimEnd() &&
                             ( mAnimEndFrame < 0 || mUsePlayerAnimator->getAnimFrame() < mAnimEndFrame ) ) )
                        return true;
        }
        else
        {
                if ( mUsePlayerAnimator->isAnimEnd() )
                        return true;
                if ( ( mAnimEndFrame < 0 ) )
                        return false;
                if ( !( mUsePlayerAnimator->getAnimFrame() < mAnimEndFrame ) )
                        return true;
        }
        return false;
}
```


