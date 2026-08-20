#pragma once
#include <Execute/alExecuteDirector.h>

namespace al
{
class ClippingActorHolder;

class ClippingDirector : public IUseExecutor
{
private:
        int                  _4;
        ClippingActorHolder* mClippingActorHolder;
        void*                _C;
        void*                _10;

public:
        void endInit();

        ClippingActorHolder* getClippingActorHolder()
        {
                return mClippingActorHolder;
        }

public:
        virtual void execute();

public:
        ClippingDirector( int );
};

} // namespace al
