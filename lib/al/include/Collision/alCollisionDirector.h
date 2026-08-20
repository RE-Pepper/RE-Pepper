#pragma once

#include <Execute/alExecuteDirector.h>

namespace al
{

class CollisionDirector : public IUseExecutor
{
private:
        void* _4;
        int   _8;
        int   _C;
        void* _10;
        void* _14;
        void* _18;

public:
        void endInit();

public:
        virtual void execute();

public:
        CollisionDirector();
};

} // namespace al
