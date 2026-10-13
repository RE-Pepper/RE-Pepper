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
