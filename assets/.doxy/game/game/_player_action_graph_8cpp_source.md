

# File PlayerActionGraph.cpp

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**src**](dir_47d28cd3eb946f860e1fe0f4e720b9c2.md) **>** [**Player**](dir_9f791c72b7e31512581b67600bde1506.md) **>** [**PlayerActionGraph.cpp**](_player_action_graph_8cpp.md)

[Go to the documentation of this file](_player_action_graph_8cpp.md)


```C++
#include "Player/PlayerActionGraph.h"

#include "Player/PlayerAction.h"
#include "Player/PlayerActionNode.h"

#ifdef NON_MATCHING
void PlayerActionGraph::move()
{
        mCurrentNode->getAction()->update();
}
#endif
```


