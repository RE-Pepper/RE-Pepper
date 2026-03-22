

# File PlayerActionMultiCondition.cpp

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**src**](dir_47d28cd3eb946f860e1fe0f4e720b9c2.md) **>** [**Player**](dir_9f791c72b7e31512581b67600bde1506.md) **>** [**PlayerActionMultiCondition.cpp**](_player_action_multi_condition_8cpp.md)

[Go to the documentation of this file](_player_action_multi_condition_8cpp.md)


```C++
#include "Player/PlayerActionMultiCondition.h"

PlayerActionMultiCondition::PlayerActionMultiCondition()
{
        mConditions.initOffset( sead::OffsetListNode<PlayerActionCondition*>::getListNodeOffset() );
}

void PlayerActionMultiCondition::append( PlayerActionCondition* condition )
{
        mConditions.pushBack( *new sead::OffsetListNode<PlayerActionCondition*>( condition ) );
}

#ifdef NON_MATCHING
bool PlayerActionMultiCondition::check()
{
        return true;
}
#endif

#ifdef NON_MATCHING
// really very incorrect
void PlayerActionMultiCondition::setup()
{
        for ( sead::OffsetList<PlayerActionCondition*>::iterator cur = mConditions.begin();
                cur != mConditions.end();
                ++cur )
                ( *cur )->setup();
}
#endif
```


