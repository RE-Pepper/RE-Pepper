#pragma once

namespace al
{

class LiveActorKit;
class ExecuteDirector;

class LayoutInitInfo
{
public:
        ExecuteDirector* mExecuteDirector;
        void*            unk[ 2 ];

        LayoutInitInfo();
};

void initLayoutInitInfo( LayoutInitInfo* info, LiveActorKit* ); // why LiveActorKit ?

} // namespace al
