

# File alNerveActionCtrl.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Nerve**](dir_0d638fa675477dde0733aed9f19ea6f2.md) **>** [**alNerveActionCtrl.h**](al_nerve_action_ctrl_8h.md)

[Go to the documentation of this file](al_nerve_action_ctrl_8h.md)


```C++
#pragma once

#include <Nerve/alNerve.h>

namespace alNerveFunction
{
class NerveActionCollector;
} // namespace alNerveFunction

namespace al
{

class LiveActor;
class NerveActionCtrl;

class NerveAction : public Nerve
{
        friend class alNerveFunction::NerveActionCollector;
        friend class NerveActionCtrl;

private:
        NerveAction* mNextNode;

public:
        virtual const char* getName() const = 0;

public:
        NerveAction();
};
} // namespace al

namespace alNerveFunction
{

class NerveActionCollector
{
        friend class al::NerveActionCtrl;

private:
        int              mNumNodes;
        al::NerveAction* mStartNode;
        al::NerveAction* mEndNode;

        static NerveActionCollector* sCurrentCollector;

public:
        void addNerve( al::NerveAction* nerve );

        static NerveActionCollector* getCurrentCollector()
        {
                return sCurrentCollector;
        }

public:
        NerveActionCollector();
};

} // namespace alNerveFunction

namespace al
{

class NerveActionCtrl
{
private:
        int           mNumNerveActions;
        NerveAction** mNerveActions;

public:
        NerveAction* findNerve( const char* pName ) const;

public:
        NerveActionCtrl( alNerveFunction::NerveActionCollector* collector );
};

} // namespace al

#define NERVEACTION_DEF( CLASS, ACTION )                                         \
        struct CLASS##Nrv##ACTION : public ::al::NerveAction                     \
        {                                                                        \
                virtual void execute( ::al::NerveKeeper* keeper ) const          \
                {                                                                \
                        static_cast<CLASS*>( keeper->getHost() )->exe##ACTION(); \
                }                                                                \
                virtual const char* getName() const                              \
                {                                                                \
                        return #ACTION;                                          \
                }                                                                \
        };                                                                       \
        const staticd( CLASS##Nrv##ACTION ) ACTION = CLASS##Nrv##ACTION();

#define NERVEACTION_DEF_END( CLASS, ACTION, ENDACTION )                             \
        struct CLASS##Nrv##ACTION : public ::al::NerveAction                        \
        {                                                                           \
                virtual void execute( ::al::NerveKeeper* keeper ) const             \
                {                                                                   \
                        static_cast<CLASS*>( keeper->getHost() )->exe##ACTION();    \
                }                                                                   \
                virtual void executeOnEnd( ::al::NerveKeeper* keeper ) const        \
                {                                                                   \
                        static_cast<CLASS*>( keeper->getHost() )->exe##ENDACTION(); \
                }                                                                   \
                virtual const char* getName() const                                 \
                {                                                                   \
                        return #ACTION;                                             \
                }                                                                   \
        };                                                                          \
        const staticd( CLASS##Nrv##ACTION ) ACTION = CLASS##Nrv##ACTION();
```


