#pragma once

#include <Nerve/alNerveExecutor.h>

namespace al
{

class NerveStateBase : public NerveExecutor
{
private:
        bool mIsDead;

public:
        inline bool isDead() const
        {
                return mIsDead;
        }

public:
        virtual void init();
        virtual void appear();
        virtual void kill();
        virtual bool update();
        virtual void control();

public:
        NerveStateBase( const char* name );
};

} // namespace al
