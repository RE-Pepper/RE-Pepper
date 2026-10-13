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
