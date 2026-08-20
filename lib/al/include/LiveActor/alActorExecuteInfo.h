#pragma once

namespace al
{

class ExecuteRequestKeeper;

class ActorExecuteInfo
{
private:
        ExecuteRequestKeeper* mRequestKeeper;

public:
        ExecuteRequestKeeper* getRequestKeeper() const
        {
                return mRequestKeeper;
        }
};

} // namespace al
