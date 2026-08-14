def create_migration_plan(infrastructure):

    plan = [
        {
            "phase": "1. Assessment",
            "activities": "Analyze existing application, infrastructure, data, and dependencies."
        },
        {
            "phase": "2. Architecture Planning",
            "activities": "Define the target cloud architecture and required Azure services."
        },
        {
            "phase": "3. Data Migration",
            "activities": "Prepare, transfer, and validate application data."
        },
        {
            "phase": "4. Application Migration",
            "activities": "Move application components to the target cloud environment."
        },
        {
            "phase": "5. Testing",
            "activities": "Validate functionality, performance, security, and availability."
        },
        {
            "phase": "6. Deployment",
            "activities": "Deploy the application to the production environment."
        },
        {
            "phase": "7. Monitoring",
            "activities": "Monitor application health and optimize the deployed solution."
        }
    ]

    return plan