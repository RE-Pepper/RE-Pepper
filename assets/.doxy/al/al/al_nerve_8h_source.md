

# File alNerve.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Nerve**](dir_0d638fa675477dde0733aed9f19ea6f2.md) **>** [**alNerve.h**](al_nerve_8h.md)

[Go to the documentation of this file](al_nerve_8h.md)


```C++
#pragma once

#include <Nerve/alNerveExecutor.h>

namespace al
{

class NerveKeeper;

struct Nerve
{
        virtual void execute( NerveKeeper* nerveKeeper ) const = 0;
        virtual void executeOnEnd( NerveKeeper* nerveKeeper ) const {};
};

#define NERVE_DEF( CLASS, ACTION )                                               \
        struct CLASS##Nrv##ACTION : public ::al::Nerve                           \
        {                                                                        \
                virtual void execute( ::al::NerveKeeper* keeper ) const          \
                {                                                                \
                        static_cast<CLASS*>( keeper->getHost() )->exe##ACTION(); \
                }                                                                \
        };                                                                       \
        const split( CLASS##Nrv##ACTION ) ACTION = CLASS##Nrv##ACTION();

#define NERVE_DEF_END( CLASS, ACTION, ENDACTION )                                   \
        struct CLASS##Nrv##ACTION : public ::al::Nerve                              \
        {                                                                           \
                virtual void execute( ::al::NerveKeeper* keeper ) const             \
                {                                                                   \
                        static_cast<CLASS*>( keeper->getHost() )->exe##ACTION();    \
                }                                                                   \
                virtual void executeOnEnd( ::al::NerveKeeper* keeper ) const        \
                {                                                                   \
                        static_cast<CLASS*>( keeper->getHost() )->exe##ENDACTION(); \
                }                                                                   \
        };                                                                          \
        const split( CLASS##Nrv##ACTION ) ACTION = CLASS##Nrv##ACTION();

#ifdef SPLIT_HACK
#undef SPLIT_HACK
#endif

} // namespace al
```


