

# File PlayerActionNode.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Player**](dir_c3d399ad73eabae4c9209488b7fe7035.md) **>** [**PlayerActionNode.h**](_player_action_node_8h.md)

[Go to the documentation of this file](_player_action_node_8h.md)


```C++
#pragma once

#include <container/seadListImpl.h>

class PlayerAction;

class PlayerActionNode
{
private:
        PlayerAction*  mAction;
        sead::ListImpl mList;

public:
        PlayerAction* getAction() const
        {
                return mAction;
        }

        virtual ~PlayerActionNode();
};
```


