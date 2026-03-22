#include "System/Application.h"

#ifdef NON_MATCHING
SEAD_SINGLETON_DISPOSER_IMPL( Application )

Application* al::getApplication()
{
        return Application::instance();
}
#endif
