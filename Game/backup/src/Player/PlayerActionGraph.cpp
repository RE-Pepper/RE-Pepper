#include "Player/PlayerActionGraph.h"

#include "Player/PlayerAction.h"
#include "Player/PlayerActionNode.h"

#ifdef NON_MATCHING
void PlayerActionGraph::move()
{
        mCurrentNode->getAction()->update();
}
#endif
