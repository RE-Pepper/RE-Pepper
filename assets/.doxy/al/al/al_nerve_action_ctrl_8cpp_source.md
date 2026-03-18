

# File alNerveActionCtrl.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Nerve**](dir_32e08f09dddceca537f9274884ee9aa2.md) **>** [**alNerveActionCtrl.cpp**](al_nerve_action_ctrl_8cpp.md)

[Go to the documentation of this file](al_nerve_action_ctrl_8cpp.md)


```C++
#include <Nerve/alNerveActionCtrl.h>
#include <Util/alStringUtil.h>

// instruction order (5)

#ifdef NON_MATCHING
al::NerveAction::NerveAction() : mNextNode( nullptr )
{
        alNerveFunction::NerveActionCollector::getCurrentCollector()->addNerve( this );
}
#endif

namespace alNerveFunction
{

NerveActionCollector* split( NerveActionCollector::sCurrentCollector );

NerveActionCollector::NerveActionCollector()
    : mNumNodes( 0 ), mStartNode( nullptr ), mEndNode( nullptr )
{
        sCurrentCollector = this;
}

void NerveActionCollector::addNerve( al::NerveAction* nerve )
{
        if ( mStartNode == nullptr )
        {
                mStartNode = nerve;
                mEndNode   = nerve;
        }
        else
        {
                mEndNode->mNextNode = nerve;
                mEndNode            = nerve;
        }
        mNumNodes++;
}

} // namespace alNerveFunction

namespace al
{

NerveActionCtrl::NerveActionCtrl( alNerveFunction::NerveActionCollector* collector )
    : mNumNerveActions( 0 ), mNerveActions( nullptr )
{
        mNumNerveActions = collector->mNumNodes;
        mNerveActions    = new NerveAction*[ mNumNerveActions ];

        // uglily copies from linked list to pointer array
        NerveAction* cur = collector->mStartNode;
        int          i   = mNumNerveActions <= 0 ? 0 : mNumNerveActions & 1;
        if ( i == 1 )
        {
                mNerveActions[ 0 ] = cur;
                cur                = cur->mNextNode;
        }
        if ( i < mNumNerveActions )
                do
                {
                        mNerveActions[ i ]     = cur;
                        cur                    = cur->mNextNode;
                        mNerveActions[ i + 1 ] = cur;
                        cur                    = cur->mNextNode;
                        i += 2;
                } while ( i < mNumNerveActions );
}

NerveAction* NerveActionCtrl::findNerve( const char* pName ) const
{
        for ( int i = 0; i < mNumNerveActions; i++ )
        {
                NerveAction* cur  = mNerveActions[ i ];
                const char*  name = cur->getName();
                if ( isEqualString( name, pName ) )
                        return cur;
        }
        return nullptr;
}

} // namespace al
```


