

# File PlayerActionGraph.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Player**](dir_c3d399ad73eabae4c9209488b7fe7035.md) **>** [**PlayerActionGraph.h**](_player_action_graph_8h.md)

[Go to the documentation of this file](_player_action_graph_8h.md)


```C++
#pragma once

class PlayerActionNode;

class PlayerActionGraph
{
private:
        PlayerActionNode* mCurrentNode;

public:
        PlayerActionNode* getCurrentNode() const
        {
                return mCurrentNode;
        }

        void move();
};
```


